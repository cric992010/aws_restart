/**
 * Class Untitled
 */
public class Javitabonito {
	
	
	public void m1trabajo (String text){
		StringBuilder textNuevo = new StringBuilder(text);
		
		textNuevo.reverse();
		
		System.out.print(textNuevo);
	}
	
	
	public static void main(String[] args) {
		Javitabonito main = new Javitabonito();
		
		main.m1trabajo("Christian");	
	}
}