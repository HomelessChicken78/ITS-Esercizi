package java3.design_pattern.composite.directory;

public class Main {
    public static void main(String[] args) {
        File file1 = new File(100);
        File file2 = new File(200);

        Directory dir1 = new Directory();
        dir1.addResource(file1);
        dir1.addResource(file2);

        Directory dir2 = new Directory();
        dir2.addResource(dir1);

        System.out.println("Total size of dir2: " + dir2.getSize());
    }
}
