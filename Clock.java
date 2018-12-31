import java.text.SimpleDateFormat;
import java.util.Date;

public class Clock{
    private DateFormat dateFormat;
    private date = new Date();

    public Clock(){
        dateFormat = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss");
    }
    
    public void showTime(){
        system.out.println(dateFormat.format(date));        
    }

        
}
