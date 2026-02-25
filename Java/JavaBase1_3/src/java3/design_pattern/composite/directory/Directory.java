package java3.design_pattern.composite.directory;

import java.util.ArrayList;
import java.util.List;

public class Directory extends Resource {
	List<Resource> subResources = new ArrayList<>();

	public Directory() {
	}

	@Override
	public int getSize() {
		int totSize = 0;

		for (Resource resource : subResources)
			totSize += resource.getSize();

		return totSize;
	}

	public void addResource(Resource resource) {
        subResources.add(resource);
    }

    public void removeResource(Resource resource) {
        subResources.remove(resource);
    }
}
