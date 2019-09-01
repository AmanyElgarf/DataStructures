package cs111;

import java.util.ArrayList;
import java.util.List;

public class BinaryTreeTraversal {
	List<Integer> inorder = new ArrayList<>();
	List<Integer> preorder = new ArrayList<>();
	List<Integer> postorder = new ArrayList<>();

	BinaryTreeTraversal(){
		inorder = new ArrayList<>();
		preorder = new ArrayList<>();
		postorder = new ArrayList<>();
	}
	
	public class TreeNode{
		TreeNode left;
		TreeNode right;
		int val;
	}
	
	public List<Integer> inorderTraversal(TreeNode root){
		if( root != null) {
			inorderTraversal(root.left);
			inorder.add(root.val);
			inorderTraversal(root.right);
		}
		return inorder;
	}
	
	
	public List<Integer> preorderTraversal(TreeNode root){
		if( root != null) {
			preorder.add(root.val);
			inorderTraversal(root.left);
			inorderTraversal(root.right);
		}
		return preorder;
	}
	
	
	public List<Integer> postorderTraversal(TreeNode root){
		if( root != null) {
			inorderTraversal(root.left);
			inorderTraversal(root.right);
			postorder.add(root.val);
		}
		return postorder;
	}

}
