from opcua import Client
import datetime
url = "opc.tcp://container.cte-gie.fr:34982"
client = Client(url)
client.connect()

root = client.get_root_node()

def display_node_tree(node, level, max_level):
    indent = "  " * level  # Indentation for tree structure
    print(f"{indent}- {node.get_display_name().Text} (NodeId: {node.nodeid}) - {[m.get_display_name() for m in node.get_methods()]}")
    start_time = datetime.datetime.now() - datetime.timedelta(days=100)
    end_time = datetime.datetime.now()
    history_data = node.read_raw_history(start_time, end_time)
    print(str(history_data))
    for data in history_data:
        print(f"Timestamp: {data.SourceTimestamp}, Value: {data.Value.Value}")
    children = node.get_children()
    if level < max_level:
        for child in children:
            display_node_tree(child, level + 1, max_level)

root.get_methods()
display_node_tree(root, 0, 5)
client.disconnect()
# out = open("out.txt", "w")
