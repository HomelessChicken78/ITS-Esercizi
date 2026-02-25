package java3.design_pattern.composite.esempio;

public abstract class Component {
	String name;

	public Component(String name) {
		this.name = name;
	}

	public abstract String operation();

	public abstract void add(Component el);

	public abstract void remove(Component el);

	public abstract Component getChild(int index);

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}
}
