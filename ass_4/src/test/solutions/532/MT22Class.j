.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static days I

.method public static DayOfWeek(I)Ljava/lang/String;
Label0:
	iload_0
	iconst_0
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	ldc "Sunday"
	areturn
	goto Label5
Label4:
	iload_0
	iconst_1
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label8
	ldc "Monday"
	areturn
	goto Label9
Label8:
	iload_0
	iconst_2
	if_icmpne Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label12
	ldc "Tuesday"
	areturn
	goto Label13
Label12:
	iload_0
	iconst_3
	if_icmpne Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label16
	ldc "Wednesday"
	areturn
	goto Label17
Label16:
	iload_0
	iconst_4
	if_icmpne Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ifle Label20
	ldc "Thursday"
	areturn
	goto Label21
Label20:
	iload_0
	iconst_5
	if_icmpne Label22
	iconst_1
	goto Label23
Label22:
	iconst_0
Label23:
	ifle Label24
	ldc "Friday"
	areturn
	goto Label25
Label24:
	iload_0
	bipush 6
	if_icmpne Label26
	iconst_1
	goto Label27
Label26:
	iconst_0
Label27:
	ifle Label28
	ldc "Saturday"
	areturn
Label28:
Label25:
Label21:
Label17:
Label13:
Label9:
Label5:
	ldc "Wrong day range"
	areturn
Label1:
	return
.limit stack 36
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MT22Class.days I
	invokestatic MT22Class/DayOfWeek(I)Ljava/lang/String;
	invokestatic io/printString(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
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
	bipush 10
	putstatic MT22Class/days I
Label1:
	return
.limit stack 2
.limit locals 0
.end method
