// JavaScript Practice 3: Climbing Stairs

// Instructions:
// Please create your solutions with JavaScript Language and put it on your new repository. And send your repository link through this forum. Don't forget to add your name and class information in readme.md file
 
// Problems:
// A staircase is given with a non-negative cost per each step. Once you pay the cost, you can either climb one or two steps. Create a solution to find the minimum sum of costs to reach the top (finishing the payments including cost[-2] or cost[-1]). You can either start at cost[0] or cost[1].
 
// Examples:
// climbingStairs([0, 2, 2, 1]) ➞ 2
// climbingStairs([0, 2, 3, 2]) ➞ 3
// climbingStairs([10, 15, 20]) ➞ 15
// climbingStairs([0, 0, 0, 0, 0, 0]) ➞ 0
 
// Clue:
// Let dp[i] be the cost to climb the i-th staircase to from 0-th or 1-th step. Hence dp[i] = cost[i] + min(dp[i-1], dp[i-2]). Since dp[i-1] and dp[i-2] are needed to compute the cost of traveling from i-th step, a bottom-up approach can be used to solve the problem. The answer will be the minimum cost of reaching n-1th stair and n-2th stair. Compute the dp[] array in a bottom-up manner.

const climbingStairs = (costStep) => {
    for (let i = costStep.length - 3; i >= 0; i--) {
        costStep[i] += Math.min(costStep[i + 1], costStep[i + 2]);
    }
    console.log(Math.min(costStep[0], costStep[1]));
};
  
climbingStairs([0, 2, 2, 1]);