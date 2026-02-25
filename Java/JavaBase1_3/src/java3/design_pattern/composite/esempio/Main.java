package java3.design_pattern.composite.esempio;

public class Main {
    public static void main(String[] args) {
        Component leaf1 = new Leaf("Leaf 1");
        Component leaf2 = new Leaf("Leaf 2");
        Component leaf3 = new Leaf("Leaf 3");

        Composite composite = new Composite("Composite");

        composite.add(leaf1);
        composite.add(leaf2);
        composite.add(leaf3);

        System.out.println("Composite operation result: " + composite.operation());

        Composite nestedComposite = new Composite("Nested Composite");
        nestedComposite.add(new Leaf("Leaf 4"));
        nestedComposite.add(new Leaf("Leaf 5"));

        composite.add(nestedComposite);

        System.out.println("Updated composite operation result: " + composite.operation());
    }
}