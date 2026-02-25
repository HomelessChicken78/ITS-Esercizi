package java3.design_pattern.composite.esempio;

public class Leaf extends Component {
	public Leaf(String name) {
		super(name);
	}

	@Override
	public String operation() {
		return name;
	}

	@Override
	public void add(Component el) {
		
	}

	@Override
	public void remove(Component el) {
		
	}

	@Override
	public Component getChild(int index) {
		return this;
	}
}
