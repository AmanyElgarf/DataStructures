public class MinHeap{
	
	int Heap[];
	int size;
	int currentSize;
	
	public MinHeap(){
		this.size = 10;
		this.Heap = new int[this.size];
		this.Heap[0] = 0;
		currentSize = 0;
	}	
	
	private int parentpos(int childPos) {
		return childPos/2;
	}
	
	private int leftChildPos(int parentPos) {
		return parentPos * 2;
	}
	
	private int rightChildPos(int parentPos) {
		return (parentPos * 2) + 1;
	}
	
	private boolean isLeaf(int pos) {
		if (pos <= currentSize/2) {
			return false;
		}
		return true;
	}
	
	private void doubleArray() {
		int newSize = 2 * size;
		int newArray[] = new int [newSize];
		for (int i = 0; i<size; i++) {
			newArray[i] = Heap[i];
		}
		size = newSize;
		Heap = newArray;
	}
	
	private void swap(int parentPos, int childPos) {
		int parent = Heap[parentPos];
		Heap[parentPos] = Heap[childPos];
		Heap[childPos] = parent;

	}
	
	private void swim(int childPos) {
		while (Heap[parentpos(childPos)] > Heap[childPos] && childPos > 1) {
			swap(parentpos(childPos), childPos);
			childPos = parentpos(childPos);
		}
	}
	
	private void sink(int parentPos) {
		while ((Heap[parentPos] > Heap[leftChildPos(parentPos)] || Heap[parentPos] > Heap[rightChildPos(parentPos)]) && isLeaf(parentPos) == false) {
			if(Heap[parentPos] > Heap[leftChildPos(parentPos)]) {
				swap(parentPos,leftChildPos(parentPos));
				parentPos = leftChildPos(parentPos);
			}
			else if (Heap[parentPos] > Heap[rightChildPos(parentPos)]) {
				swap(parentPos,rightChildPos(parentPos));
				parentPos = rightChildPos(parentPos);
			}
		}
	}
	
	
	
	public void insert(int element) {
		if (currentSize + 1 == size) {
			doubleArray();
		}
		Heap[++currentSize] = element;
		swim(currentSize);
	}
	
	public int getMin() {
		return Heap[1];
	}
	
	public void delMin() {
		swap(1, currentSize);
		currentSize --;
		sink(1);
	}

	public void print () {
		for (int i = 1; i <= currentSize; i++) {
			System.out.println(Heap[i]);
		}
	}
}