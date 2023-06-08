class Vehicle {
    int speed = 50;
}
 
public class Bike2 extends Vehicle {
    int speed = 100;
 
    void display() {
        System.out.println(super.speed);//in speed của lớp Vehicle  
    }
 
    public static void main(String args[]) {
        Bike2 b = new Bike2();
        b.display();
 
    }
}