package Leetcode;

import java.util.*;


public class WordLadder {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        Queue<String> queue = new LinkedList<>(); // Queue to do BFS of the graph we are going to build.
        Set<String> wordSet = new HashSet<>(wordList); // NOTE THIS IS HOW YOU ADD A LIST OF WORDS TO HASHSET!
        wordSet.remove(beginWord); // Remove the beginning word from set
        queue.add(beginWord); // Add it to queue to build first level
        int level = 0;

        while (!queue.isEmpty()) {
            level++; // Increment level as we iterate
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                String currentWord = queue.poll(); // Current word node at level
                if (currentWord.equals(endWord)) return level; // Found the endWord in the queue so we are done
                List<String> allSeqList = findSeqs(currentWord); // Get an array holding all possible sequences
                for (String s: allSeqList) { //For every possible sequence in the array in respect to currentword
                    if (wordSet.contains(s)) { // If the particular sequence is in the hashSet
                        wordSet.remove(s); // Remove that element from the hashset as we have visited it
                        queue.add(s); //Add it to the next level of the queue.
                    }
                }
            }
        } return 0;
    }

    public static List<String> findSeqs(String currentWord) {
        char[] charArray = currentWord.toCharArray(); // Make a list of chars so each individual char from cWord
        List<String> allPossSeqs = new ArrayList<>(); // Array to hold all combinations of the word
        for (int i = 0; i < charArray.length; i++) { // For every single CHAR in the passed word. This is important because recall we want to change EVERY single char to get ALL possible combinations.
            char temp = charArray[i]; // We need a temp char so we can eventually revert back.
            for (char c = 'a'; c <= 'z'; c++) { // This sets c to go from a - z hence the entire alphabet
                charArray[i] = c; // Make the CURRENT char we are looking at = to each alphabet character
                String nextSeq = new String(charArray);// Convert the current charArray WITH the transformed letter to a string and add that string to all possible sequences array.
                allPossSeqs.add(nextSeq); // Add this combination to our combinations array
            }
            charArray[i] = temp; // Revert the character back to original and move onto the next one in the word.
        }
        return allPossSeqs; // Return array of all possible combinations of passed argument currentWord
    }
}

