JFLAGS = -g
JC = javac
.SUFFIXES: .java .class
.java.class:
	$(JC) $(JFLAGS) $*.java

CLASSES = \
		lox/AstPrinter.java \
		lox/Expr.java \
		lox/Interpreter.java \
		lox/Lox.java \
		lox/Parser.java \
		lox/Scanner.java \
		lox/Stmt.java \
		lox/Token.java \
		lox/TokenType.java \
		tools/GenerateAst.java


default: classes

classes: $(CLASSES:.java=.class)

clean:
	$(RM) *.class
