.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static arr [[[[[I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MT22Class/arr [[[[[I
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_0
	iaload
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 7
.limit locals 1
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
	iconst_1
	iconst_1
	iconst_1
	iconst_2
	iconst_2
	multianewarray [[[[[I 5
	putstatic MT22Class/arr [[[[[I
	getstatic MT22Class/arr [[[[[I
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_0
	bipush 40
	iastore
	getstatic MT22Class/arr [[[[[I
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_1
	bipush 50
	iastore
	getstatic MT22Class/arr [[[[[I
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_1
	aaload
	iconst_0
	bipush 60
	iastore
	getstatic MT22Class/arr [[[[[I
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_1
	aaload
	iconst_1
	bipush 70
	iastore
Label1:
	return
.limit stack 12
.limit locals 0
.end method
