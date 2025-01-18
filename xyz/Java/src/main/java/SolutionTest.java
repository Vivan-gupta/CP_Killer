import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.TimeoutException;

public class SolutionTest
{
  static Solution solution = new Solution();
  public static void main(String[] args)
  {
      Object[] result0 = Testcase_0();
      Object[] result1 = Testcase_1();
      Object[] result2 = Testcase_2();

      boolean RE_found = (boolean) result0[0] || (boolean) result1[0] || (boolean) result2[0];
      boolean allPass = (boolean) result0[1] && (boolean) result1[1] && (boolean) result2[1];

      StringBuilder messageBuilder = new StringBuilder();
      messageBuilder.append(result0[2]).append("\n")
                    .append(result1[2]).append("\n")
                    .append(result2[2]).append("\n");

      if (!allPass)
          System.out.println(messageBuilder.toString());
      System.out.println(allPass);
      System.out.println(RE_found);
  }

   // Constrain testing testcase
   public static Object[] Testcase_0()
   {
       int sample_try = 0;
       boolean RE_found = false;
       boolean TLE_found = false;
       String message = "";
       while(sample_try < 50)
       {
           int m = 1 + (int)(Math.random() * 100);
           int n = 1 + (int)(Math.random() * 100);
           int[][] grid = new int[m][n];
           for (int i = 0; i < m; i++) {
               for (int j = 0; j < n; j++) {
                   grid[i][j] = 1 + (int)(Math.random() * 4);
               }
           }
           try
           {
               CompletableFuture.supplyAsync(() -> solution.minCost(grid)).get(2, TimeUnit.SECONDS);
           }
           catch (TimeoutException | InterruptedException e)
           {
               TLE_found = true;
               message += "Input: Random grid with dimensions (" + m + ", " + n + ")\nOutput: Time Limit Exceeded\n";
               break;
           }
           catch (ExecutionException e)
           {
              RE_found = true;
              message += "Input: Random grid with dimensions (" + m + ", " + n + ")\nOutput: " + e.getCause() + "\n";
              break;
           }
           sample_try++;
       }
       return new Object[]{RE_found, !(TLE_found || RE_found), message};
   }

   // Testcase 1
   public static Object[] Testcase_1() {
      int result;
      int expected = 3;
      boolean isPass = true;
      boolean TLE_found = false;
      boolean RE_found = false;
      String output;
      int[][] input = {{1,1,1,1},{2,2,2,2},{1,1,1,1},{2,2,2,2}};

      try
      {
           result = CompletableFuture.supplyAsync(() -> solution.minCost(input)).get(2, TimeUnit.SECONDS);
           isPass = result == expected;
           output = Integer.toString(result);
      }
      catch (TimeoutException | InterruptedException e)
      {
           TLE_found = true;
           isPass = false;
           output = "Time Limit Exceeded";
      }
      catch (ExecutionException e)
      {
           RE_found = true;
           isPass = false;
           output = e.getCause().toString();
      }
      String message = "Input: [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]\nExpected Output: 3\nOutput: " + output;
      return new Object[]{RE_found, isPass, message};
  }

  // Testcase 2
  public static Object[] Testcase_2() {
      int result;
      int expected = 0;
      boolean isPass = true;
      boolean TLE_found = false;
      boolean RE_found = false;
      String output;
      int[][] input = {{1,1,3},{3,2,2},{1,1,4}};

      try
      {
           result = CompletableFuture.supplyAsync(() -> solution.minCost(input)).get(2, TimeUnit.SECONDS);
           isPass = result == expected;
           output = Integer.toString(result);
      }
      catch (TimeoutException | InterruptedException e)
      {
           TLE_found = true;
           isPass = false;
           output = "Time Limit Exceeded";
      }
      catch (ExecutionException e)
      {
           RE_found = true;
           isPass = false;
           output = e.getCause().toString();
      }
      String message = "Input: [[1,1,3],[3,2,2],[1,1,4]]\nExpected Output: 0\nOutput: " + output;
      return new Object[]{RE_found, isPass, message};
  }
}