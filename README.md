# This project is building a re-inforcement learning scrabble agent 
## Current State : 
Implemented Direct Acrylic Word Graph (DAWG) object to compress scrabble dictionary into light weight and easily searchable data structure.
This will allow the agent to search all possible actions quickly which will decrease training time and allow for the game to be deployed with minimal memory usage on a web browser.

## Next Steps: 
 1. Re-Write DAWG object in c++ to reduce memory consumption
 2. Add score of word into the end of word pointer in DAWG object
 3. Create search function to determine possible moves based on scrabble board state (potential solution https://github.com/dqlynch/scrabblesolver/blob/master/scrabble_solver/solver.py)
 4. Research effective RL/deterministic techniques and algorithms to improve agents decision making
    - Worst case algorithm will select highest scoring word based on possible set of moves
 
 
 
 References:
 - http://stevehanov.ca/blog/?id=115
 - http://iswsa.acm.org/mphf/index.html
 - https://github.com/fayrose/Scrabble
 - https://github.com/dqlynch/scrabblesolver/tree/master/scrabble_solver
 
