/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
const wordBreak = (s, wordDict) => {
  const wordDictCharacterMap = {}
  for (const word of wordDict) {
    word.split("").forEach(c => (wordDictCharacterMap[c] = true));
  }

  for (const c of s) {
    if (!(c in wordDictCharacterMap))
      return false;
  }
  return solveBacktrack(s, wordDict);
};

/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
const solveBacktrack = (s, wordDict) => {
  if (s.length == 0) return true;
  let success = false;
  for (const word of wordDict) {
    if (s.startsWith(word)) {
      success = success || wordBreak(s.substring(word.length), wordDict);
    }
  }
  return success;
}


