import json
from typing import List, Tuple, Union


def to_tree(source: List[Union[Tuple[None, str], Tuple[str, str]]]) -> str:
    """
    Builds a tree based on the passed list of tuples.

    :param source: List of tuples of (parent id, child id) format.
    When node id is None it is a root node.
    :return: Dictionary converted to JSON string with keys started
    from the children of the root node and dictionaries as values
    """
    # Find tuples with a root parent
    root_children = [tup for tup in source if tup[0] is None]

    # If there are no such tuple we need to fix the input data
    if not root_children:
        msg = 'Can not build a tree without a root node. There should be at least one pair with parent None'
        raise TypeError(msg)

    # Clean up the source for further steps
    # by removing the tuples with root parent
    for pair in root_children:
        source.remove(pair)

    # Store the keys for the final tree (in our example: 'a', 'b', 'c')
    temp_roots = set()
    # Store values for each node
    temp_storage = {}

    for parent, child in source:

        # For every new child entry in temporary storage
        # create a key-value pair with empty dictionary as value
        child_value = temp_storage.get(child)
        if temp_storage.get(child) is None:
            child_value = {}
            temp_storage[child] = child_value
        else:
            temp_roots.discard(child)

        # For every new parent entry in temporary storage create a key-value pair
        # with dictionary containing child entry of temporary storage from above
        parent_value = temp_storage.get(parent)
        if parent_value is None:
            temp_storage[parent] = {child: child_value}
            temp_roots.add(parent)
        else:
            # If the value for this parent already exists just update it
            parent_value[child] = child_value

    # Building a tree: temporary roots are the keys
    tree = {node: temp_storage[node] for node in temp_roots}

    # Convert to json string in order to have a nice output
    return json.dumps(tree, indent=4, sort_keys=True)
