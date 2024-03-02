package _01_StringTrimmer;

import static org.junit.Assert.assertEquals;

import org.junit.jupiter.api.Test;

public class StringTrimmerTest {

    @Test
    void TestStringTrim1() {
        assertEquals("Hello W", StringTrimmer.trimString("Hello World!", 5));
    }
    
    @Test
    void TestStringTrim2() {
        assertEquals("League", StringTrimmer.trimString("LeagueOfAmazing!", 10));
    }
    
    @Test
    void TestStringTrim3() {
        assertEquals("James", StringTrimmer.trimString("JamesTheIntern", 9));
    }
    
    @Test
    void TestStringTrim4() {
        assertEquals("", StringTrimmer.trimString("TheWholeWord", 12));
    }
}
