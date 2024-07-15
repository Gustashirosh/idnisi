def validate_operation(operation):
    if "op" not in operation:
        raise JsonPatchError("Operation does not contain 'op' field")
    if operation["op"] not in ["add", "remove", "replace", "move", "copy", "test"]:
        raise JsonPatchError("Invalid operation type")
    if "path" not in operation:
        raise JsonPatchError("Operation does not contain 'path' field")
    if operation["op"] in ["add", "replace", "test"] and "value" not in operation:
        raise JsonPatchError("Operation does not contain 'value' field")
    if operation["op"] in ["move", "copy"] and "from" not in operation:
        raise JsonPatchError("Operation does not contain 'from' field")
