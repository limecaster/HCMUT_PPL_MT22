.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static x [[I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
.var 2 is j I from Label0 to Label1
	iconst_0
	istore_2
	iconst_0
	istore_1
Label4:
	iload_1
	iconst_2
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
	iconst_0
	istore_2
Label11:
	iload_2
	iconst_2
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label10
	getstatic MT22Class/x [[I
	iload_1
	aaload
	iload_2
	iconst_4
	iastore
Label9:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label11
Label10:
Label2:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label4
Label3:
	getstatic MT22Class/x [[I
	iconst_1
	aaload
	iconst_1
	iaload
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 23
.limit locals 3
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
	iconst_2
	iconst_2
	multianewarray [[I 2
	putstatic MT22Class/x [[I
Label1:
	return
.limit stack 2
.limit locals 0
.end method
