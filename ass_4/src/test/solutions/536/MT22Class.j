.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
	iload_1
	iconst_1
	iadd
	istore_1
	iload_1
	iconst_2
	irem
	iconst_0
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label8
	goto Label2
Label8:
	iload_1
	invokestatic io/printInteger(I)V
Label2:
	iload_1
	bipush 10
	if_icmpge Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifle Label3
	iload_1
	iconst_1
	iadd
	istore_1
	iload_1
	iconst_2
	irem
	iconst_0
	if_icmpne Label13
	iconst_1
	goto Label14
Label13:
	iconst_0
Label14:
	ifle Label15
	goto Label2
Label15:
	iload_1
	invokestatic io/printInteger(I)V
	goto Label2
Label3:
Label1:
	return
.limit stack 23
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
Label1:
	return
.limit stack 0
.limit locals 0
.end method
