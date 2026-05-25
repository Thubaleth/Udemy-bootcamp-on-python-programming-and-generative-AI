"""
Route support tickets.

tickets = {
    "billing": ["payment", "refund", "invoice"],
    "technical": ["bug", "error", "crash"],
    "account": ["login", "password", "signup"]
}

Requirements:
- Ask user for support message
- Detect category
- Route ticket to correct department
"""
tickets = {
    "billing": ["payment", "refund", "invoice"],
    "technical": ["bug", "error", "crash"],
    "account": ["login", "password", "signup"]
}

tickets = {
    "billing": ["payment", "refund", "invoice"],
    "technical": ["bug", "error", "crash"],
    "account": ["login", "password", "signup"]
}

def route_ticket():

    # Ask user for a support message
    message = input("Enter your support message: ").lower()

   
    for category, keywords in tickets.items():

        for word in keywords:

            if word in message:
                print(f"Route ticket to {category} department")
                return

    # If no keyword matches
    print("No matching department found")

route_ticket()