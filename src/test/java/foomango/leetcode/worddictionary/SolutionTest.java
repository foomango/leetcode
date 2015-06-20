package foomango.leetcode.worddictionary;

import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

public class SolutionTest {
	private Solution1 s;
	
	@Before
	public void setUp() {
		s = new Solution1();
	}
	
	@Test
	public void smokeTests() {
		s.addWord("bad");
		s.addWord("dad");
		s.addWord("mad");
		s.addWord("a");
		
		assertFalse(s.search("pad"));
		assertTrue(s.search("bad"));
		assertTrue(s.search(".ad"));
		assertTrue(s.search("b.."));
		assertFalse(s.search("a."));
		assertFalse(s.search("ba"));
	}
}