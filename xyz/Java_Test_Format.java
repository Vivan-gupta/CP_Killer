import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.TimeoutException;

import required_Files

public class SolutionTest
{
  static Solution solution = new Solution();
  public static void main(String[] args)
  {
      Object[] result0 = Testcase_0()
      Object[] result1 = Testcase_1()
      Object[] result2 = Testcase_2()
      .
      .

      boolean RE_found = (boolean) result0[0] || (boolean) result1[0] || (boolean) result2[0] ...
      boolean allPass = (boolean) result0[1] && (boolean) result1[1] && (boolean) result2[1] ...

      StringBuilder messageBuilder = new StringBuilder();
      messageBuilder.append(result0[2]).append("\n")
                    .append(result1[2]).append("\n")
                    .append(result2[2]).append("\n")
              .
              .

      if (!allPass)
          System.out.println(messageBuilder.toString());
      System.out.println(allPass)
      System.out.println(RE_found)
  }

   //Constrain testing testcase
   public static Object[] Testcase_0()
   {
       int sample_try=0;
       boolean TLE_found = false
       String message="";
       while(sample_try<50)
       {
           Use Random function to generate random inputs between given contains as Example
           int xyz = (int)(Math.random()*Contain_Limit_in_Testcases);
           try
           {
               CompletableFuture.supplyAsync(() -> solution.function_in_format(randomized_input/s)).get(Time_Limit_From_Input, TimeUnit.SECONDS);
           }
           catch (TimeoutException | InterruptedException e)
           {
               TLE_found = true;
               message += "Input: " + randomized_input/s +
                         "\nOutput: Time Limit Exceeded\n";
               break;
           }
           catch (ExecutionException e)
           {
              RE_found = true
              output = e.getCause()
              message += "Input: " + randomized_input/s +
                        "\nOutput:" + e.getCause +"\n";
              break;
           }
           sample_try++;
       }
       return new Object[]{RE_found, !(TLE_found | RE_found), message};
   }
  //Testcase 1
  public static Object[] Testcase_1() {
      int result;
      int expected = Expected_Output/s_of_testcase2;
      boolean isPass = true;
      boolean TLE_found = false;
      boolean RE_found = false;
      String output;

      try
      {
           result = CompletableFuture.supplyAsync(() -> solution.function_in_format(input/s_of_testcase1)).get(Time_Limit_From_Input, TimeUnit.SECONDS);
           isPass = result == expected;
           output = .toString(result)
      }
      catch (TimeoutException | InterruptedException e)
      {
           TLE_found=true
           isPass = false
           output = "Time Limit Exceeded"
      }
      catch (ExecutionException e)
      {
           RE_found=true
           isPass = false
           output = e.getCause()
      }
      String message = "Input: " + input/s_of_testcase1 +
                       "\nExpected Output: " + Output/s_of_testcase1 +
                       "\nOutput: " + output;
      return new Object[]{RE_found, isPass, message};
  }

  //Testcase 2
  public static Object[] Testcase_2() {
      int result;
      int expected = Expected_Output/s_of_testcase2;
      boolean isPass = true;
      boolean TLE_found = false;
      boolean RE_found = false;
      String output;

      try
      {
           result = CompletableFuture.supplyAsync(() -> solution.function_in_format(input/s_of_testcase2)).get(Time_Limit_From_Input, TimeUnit.SECONDS);
           isPass = result == expected;
           output = .toString(result)
      }
      catch (TimeoutException | InterruptedException e)
      {
           TLE_found=true
           isPass = false
           output = "Time Limit Exceeded"
      }
      catch (ExecutionException e)
      {
           RE_found=true
           isPass = false
           output = e.getCause()
      }
      String message = "Input: " + input/s_of_testcase2 +
                       "\nExpected Output: " + Output/s_of_testcase2 +
                       "\nOutput: " + output";
      return new Object[]{RE_found, isPass, message};
  }
      .
      .
      .
  }
}