public class TestNull {
    public static void main(String[] args) {
        double x1 = 0., x2 = 1.6; // Startintervall
        System.out.println("Nullstelle = " + Nullstelle.find( x1, x2, new TFunc1() ));
        System.out.println("Nullstelle = " + Nullstelle.find( x1, x2, new TFunc2() ));
        System.out.println("Nullstelle = " + Nullstelle.find( x1, x2, new TFunc3() ));
}
}
