'''

    λ expressions
    
    <expression> ::= <name> | <function> | <function application>

    <name> can be any sequence of non-blank characters

    <function> ::= λ<name>.<body>

    <body> ::= <expression>
    
    <function application> ::= (<function expression> <argument expression>)
        where
            <function expression> ::= <expression>
            <argument expression> ::= <expression>

'''
