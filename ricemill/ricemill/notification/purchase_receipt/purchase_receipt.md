<html>New Purchase Receipt {{doc.name}}
*Details*

• Supplier :- {{doc.supplier}}
• Amount: {{ doc.grand_total }}
*Item Name Details*
{% for item in doc.items %}

Item Name :- {{ item.item_name }}, QTY :- {{ item.qty }}, Rejected Quantity :- {{ item.rejected_qty }}, Rate :- {{ item.rate }}, Amount :- {{ item.amount }}

{% endfor %}
• Total Quantity :- {{doc.total_qty}}
• Total :- {{doc.total}}
</html>