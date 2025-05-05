from StaticError import *
from Symbol import *
from functools import *


def simulate(list_of_commands):
    """
    Executes a list of commands and processes them sequentially.

    Args:
        list_of_commands (list[str]): A list of commands to be executed.

    Returns:
        list[str]: A list of return messages corresponding to each command.
    """

    def process_command(state, command):
        (stack, outputs) = state

        shiji = command.strip().split(' ')
        if shiji[0] == "INSERT":
           if len(shiji) != 3:
                raise InvalidInstruction(command)
           return insert(shiji[1], shiji[2], command, stack, outputs)
        elif shiji[0] == "ASSIGN":
            if len(shiji) != 3:
                raise InvalidInstruction(command)
            return assign(shiji[1], shiji[2], command, stack, outputs)
        elif shiji[0] == "BEGIN":
            if len(shiji) != 1:
                raise InvalidInstruction(command)
            return ([[]] + stack, outputs)
        elif shiji[0] == "END":
            if len(shiji) != 1:
                raise InvalidInstruction(command)
            if len(stack) <= 1:
                raise UnknownBlock()
            else:
                return (stack[1:], outputs)
        elif shiji[0] == "PRINT":
            if len(shiji) != 1:
                raise InvalidInstruction(command)
            return xprint(stack, outputs)
        elif shiji[0] == "RPRINT":
            if len(shiji) != 1:
                raise InvalidInstruction(command)
            return rprint(stack, outputs)
        elif shiji[0] == "LOOKUP":
            if len(shiji) != 2:
                raise InvalidInstruction(command)
            return lookup(shiji[1], command, stack, outputs)
        else:
            raise InvalidInstruction(command)
        

###___INSERT AND ASSIGN____####
    def insert(name, typ, command, stack, outputs):
        if not check_name(name):
            raise InvalidInstruction(command)
        if typ not in ["number", "string"]:
            raise InvalidInstruction(command)
        if any(symbol.name == name for symbol in stack[0]):
            raise Redeclared(command)
        new_scope = stack[0] + [Symbol(name, typ)]
        new_stack = [new_scope] + stack[1:]
        return (new_stack, outputs + ["success"])
    
    def assign(name, value, command, stack, outputs):
        if not check_name(name):
            raise InvalidInstruction(command)
        
        found, __ = find_symbol(stack, name)
        value_var, __ = find_symbol(stack, value)
        value_type, value_valid = get_type(value)   

        if found is None:
            if value_valid is False:
                if check_name(value):
                    raise Undeclared(command)
                if value_var is None:
                    raise InvalidInstruction(command)
            raise Undeclared(command)
        
        if value_var is not None: ## handle case when value is a variable
            if value_var.typ != found.typ:
                raise TypeMismatch(command)
            return (stack, outputs + ["success"])
            
        if value_var is None: ## handle case when value is a not a variable
            if check_name(value):
                raise Undeclared(command)
            if not value_valid:
                raise InvalidInstruction(command)
            if found.typ != value_type:
                raise TypeMismatch(command)
            return (stack, outputs + ["success"])

       
    

###___PRINT AND XPRINT____####
    def xprint(stack, outputs):
        def process_scope(stack, result_parts, index):
            if index < 0:  
                return result_parts
            return process_scope(stack, 
                                process_symbol(stack[index], result_parts, index, len(stack) - 1 - index),
                                index - 1)

        return stack, outputs + [" ".join(process_scope(stack, [], len(stack) - 1) )]
    
    def rprint(stack, outputs):
        def process_scope(stack, result_parts, index):
            if index >= len(stack):
                return result_parts
            return process_scope(stack,
                                process_symbol(stack[index], result_parts, index, len(stack) - 1 - index, True), 
                                index + 1)
        return stack, outputs + [" ".join(process_scope(stack, [], 0))]


    def process_symbol(scope, result_parts, index, level, rprint=False):
        if not scope: 
            return result_parts
        if rprint: #duyệt từ cuối scope lên
            # new_entry = scope[-1].name + "//" + str(level)
            return process_symbol(scope[:-1], 
                                  merge(result_parts, scope[-1].name + "//" + str(level), rprint), 
                                  index, level, rprint)
        else:
            # new_entry = scope[0].name + "//" + str(level)
            return process_symbol(scope[1:], 
                                  merge(result_parts, scope[0].name + "//" + str(level), rprint), 
                                  index, level)    


    def merge(list, entry, rprint=False):
        name, level = entry.split("//")
        level = int(level)
        existing = next((item for item in list if item.split("//")[0] == name), None)

        if rprint:
            return list + [entry] if not existing else list
        else:
            ans = [item for item in list if item.split("//")[0] != name]
            if existing:
                if int(existing.split("//")[1]) >= level:
                    return ans + [existing]
            return ans + [entry]
                      

###___LOOKUP____####
    def lookup(name, command, stack, outputs):
        found, level = find_symbol(stack, name)
        if found is None:
            raise Undeclared(command)
        return (stack, outputs + [str(level)])            


###___HELPER FUNCTIONS____####
    def find_symbol(stack, name, index=0):
        if index >= len(stack): 
            return None, -1
        scope = stack[index]
        found = next((symbol for symbol in scope if symbol.name == name), None)
        if found:
            return found, len(stack) - index - 1
        return find_symbol(stack, name, index + 1)
    
    def get_type(value):
        if check_number(value):
            return "number", True
        elif check_string(value):
            return "string", True
        else:
            return None, False
        
    def check_name(name):
        return (
            name[0].islower() and
            all(char.isalnum() or char.isalpha() or char == '_' for char in name[1:])
        )
    
    def check_string(value):
        return (
            value[0] == "'" and
            value[-1] == "'" and
            all(char.isalnum() or char.isalpha() or char == ' ' for char in value[1:-1])
        )
    
    def check_number(value):
        return (
            all(char.isdigit() for char in value)
        )
        
###___MAIN FUNCTION____####       
    final_stack, final_output = reduce(lambda state, cmd : process_command(state, cmd), list_of_commands, ([[]], []))
   
    if len(final_stack) != 1:
        raise UnclosedBlock(len(final_stack) -1)

    return final_output


