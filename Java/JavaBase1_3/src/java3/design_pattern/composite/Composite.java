package java3.design_pattern.composite;

import java.util.ArrayList;
import java.util.List;

public class Composite extends Component {
	List<Component> components = new ArrayList<>();

	public Composite(String name) {
		super(name);
	}

	@Override
	public String operation() {
		String res = name + " ";

		for (Component component : components) {
			res += component.operation() + " ";
		}

		return res;
	}

	@Override
	public void add(Component el) {
		components.add(el);
	}

	@Override
	public void remove(Component el) {
		components.remove(el);
	}

	@Override
	public Component getChild(int index) {
		return components.get(index);
	}
	
}
