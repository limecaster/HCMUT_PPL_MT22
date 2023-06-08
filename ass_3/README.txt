Set environment variable ANTLR_JAR to the file antlr-4.9.2-complete.jar in your computer
Change current directory to initial/src where there is file run.py
Type: python run.py gen 
Then type: python run.py test LexerSuite
Then type: python run.py test ParserSuite
Then type: python run.py test ASTGenSuite
Then type: python run.py test CheckerSuite
Then type: python run.py test CodeGenSuite

MT22 language likes Pascal, it also has some special features: 
    - Auto type like C++ for variables, parameters, functions.
    - Pass by value-result scheme thanks to "out" keyword in parameter declararion.
    - Inheritance parameter feature: Child function can inherit param from parent function by a default function "super(<list of expr>)" that assign parent inherit param to each expr correspondingly, or can deactivate this feature "prevenDefault()".
    - Multi-dimensional array: It's hard to manipulate in Intemediate CodeGenerator assignment.
Good luck for you all to pass this subject by only 1 time.
