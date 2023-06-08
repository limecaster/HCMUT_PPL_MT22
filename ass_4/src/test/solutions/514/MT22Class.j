.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static x [I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MT22Class/x [I
	iconst_0
	bipush 10
	iastore
	getstatic MT22Class/x [I
	iconst_1
	bipush 20
	iastore
	getstatic MT22Class/x [I
	iconst_2
	bipush 30
	iastore
	getstatic MT22Class/x [I
	iconst_3
	bipush 40
	iastore
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
	iconst_0
	istore_1
Label4:
	iload_1
	iconst_4
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
	getstatic MT22Class/x [I
	iload_1
	iaload
	i2f
	invokestatic io/printFloat(F)V
Label2:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label4
Label3:
Label1:
	return
.limit stack 18
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LMT22Class; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
	iconst_4
	newarray int
	putstatic MT22Class/x [I
Label1:
	return
.limit stack 1
.limit locals 0
.end method
