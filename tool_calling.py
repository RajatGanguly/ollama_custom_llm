import ollama

inventory_db = {
    "laptop": {"stock": 5, "base_price": 1200},
    "monitor": {"stock": 0, "base_price": 300},
    "keyboard": {"stock": 25, "base_price": 80}
}

# Tool defination
# Checking DB
def check_inventory(product_name):
    product_name = product_name.lower()
    if product_name in inventory_db:
        return inventory_db[product_name]
    return {"stock": 0, "base_price": None}

# Discount Logic
def calculate_loyality_discount(base_price, years_as_customer):
    discount_rate = min(years_as_customer*0.5, 0.3)
    final_price = base_price*(1-discount_rate)
    return round(final_price, 2)

# Mapping functions
available_functions = {
    "check_inventory": check_inventory, 
    "calculate_loyality_discount": calculate_loyality_discount
}

# Tool Schema
tools = [
    {
        "type": "function",
        "function": {
            "name": "check_inventory",
            "description": "Get stock and price for a product",
            "parameters": {
                "type": "object",
                "properties": {
                    "product_name": {"type": "string"}
                },
                "required": ["product_name"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate_loyality_discount",
            "description": "Calculate final price based on loyality years",
            "parameters": {
                "type": "object",
                "properties": {
                    "base_price": {"type": "number"},
                    "years_as_customer": {"type": "integer"}
                },
                "required": ["base_price", "years_as_customer"]
            }
        }
    }
]

message = [
    {"role": "user", "content": "Hello, I am Rudra. I am a 8 years old customer. I want to buy a laptop, could you please check the stock"}
]

response = ollama.chat(
    model="qwen3:8b",
    messages=message,
    tools=tools
)

print(response["message"])

tool_calls = response["message"].get("tool_calls")

if tool_calls:
    for tool_call in tool_calls:
        tool_name = tool_call["function"]["name"]
        tool_args = tool_call["function"]["arguments"]

        function_to_call = available_functions[tool_name]
        result = function_to_call(**tool_args)

        message.append(response["message"])
        message.append({
            "role": "tool",
            "content": str(result)
        })

print("\n", "*-"*24)

final_response = ollama.chat(
    model="qwen3:8b",
    messages=message
)

print(final_response)