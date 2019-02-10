/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
const wordBreak = (s, wordDict) => {
  if (s.length == 0) return true;
  let success = false;
  for (const word of wordDict) {
    if (s.startsWith(word)) {
      success = success || wordBreak(s.substring(word.length), wordDict);
    }
  }
  return success;
};

