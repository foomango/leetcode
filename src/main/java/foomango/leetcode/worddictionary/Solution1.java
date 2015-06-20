package foomango.leetcode.worddictionary;

public class Solution1 {
	private Node root = new Node();

	static class Node {
		public static final int MAX_LEN = 26;
		public Node[] nodes = new Node[MAX_LEN];
		public boolean isRealNode;
	}

	// Adds a word into the data structure.
	public void addWord(String word) {
		addWord(root, word, 0);
	}

	// Returns if the word is in the data structure. A word could
	// contain the dot character '.' to represent any one letter.
	public boolean search(String word) {

		return search(root, word, 0);
	}

	private void addWord(Node root, String word, int index) {
		if (index >= word.length()) {
			return;
		}

		int nodeIndex = word.charAt(index) - 'a';
		if (root.nodes[nodeIndex] == null) {
			root.nodes[nodeIndex] = new Node();
		}

		// last character
		if (index == word.length() - 1) {
			root.nodes[nodeIndex].isRealNode = true;
		} else {
			addWord(root.nodes[nodeIndex], word, index + 1);
		}
	}

	private boolean search(Node root, String word, int index) {
		if (index >= word.length()) {
			return false;
		}

		if (root == null) {
			return false;
		}

		char ch = word.charAt(index);

		if (ch != '.') {
			int nodeIndex = ch - 'a';
			if (root.nodes[nodeIndex] != null) {
				// last character
				if (index == word.length() - 1) {
					if (root.nodes[nodeIndex].isRealNode) {
						return true;
					} else {
						return false;
					}
				} else {
					return search(root.nodes[nodeIndex], word, index + 1);
				}
			} else {
				return false;
			}
		} else {
			// '.' is the last character in word
			if (index == word.length() - 1) {
				for (int i = 0; i < Node.MAX_LEN; i++) {
					if (root.nodes[i] != null && root.nodes[i].isRealNode) {
						return true;
					}
				}
				return false;
			} else {
				
				for (int i = 0; i < Node.MAX_LEN; i++) {
					if (search(root.nodes[i], word, index + 1)) {
						return true;
					}
				}

				return false;
			}
		}
	}
}
