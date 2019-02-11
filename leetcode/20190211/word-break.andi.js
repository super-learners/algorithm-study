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
  const cheatsheet = {};
  return solveBacktrack(s, wordDict, cheatsheet);
};

/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
const solveBacktrack = (s, wordDict, cheatsheet) => {
  if (s.length == 0) return true;
  if (s in cheatsheet) return cheatsheet[s];
  let success = false;
  for (const word of wordDict) {
    if (s.startsWith(word)) {
      success = success || solveBacktrack(s.substring(word.length), wordDict, cheatsheet);
    }
  }
  cheatsheet[s] = success;
  return success;
}
