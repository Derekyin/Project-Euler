
public class question5 {
	public static void main(String args[]){
		int x = 2519;
			boolean getNum = false;
			while(!getNum){
				if((x % 16 ==0)&&(x % 9 ==0)&&(x%5==0)&&(x%7==0)&&(x % 11 ==0)&&(x % 13 ==0)&&(x%17==0)&&(x%19==0)){
					System.out.println(x);
					getNum = true;
				}else{
					x++;
				}
			}
		}
	}

