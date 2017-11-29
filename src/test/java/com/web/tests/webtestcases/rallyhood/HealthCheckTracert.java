package com.web.tests.webtestcases.rallyhood;
///****/
//package com.web.tests.webtestcases.ifusion;
//
//import java.io.FileNotFoundException;
//import java.util.ArrayList;
//import java.util.Properties;
//
//import org.apache.logging.log4j.LogManager;
//import org.apache.logging.log4j.Logger;
//import org.openqa.selenium.WebDriver;
//import org.python.util.PythonInterpreter;
//import org.testng.ITestContext;
//import org.testng.annotations.AfterClass;
//import org.testng.annotations.BeforeClass;
//import org.testng.annotations.DataProvider;
//import org.testng.annotations.Parameters;
//import org.testng.annotations.Test;
//
//import com.innominds.team.driverinit.DriverManager;
//import com.innominds.team.frameworkengine.Constants;
//import com.innominds.team.utils.PropertyFileUtils;
//import com.web.tests.ifusion.Login;
//import com.web.tests.ifusion.LoginDP;
//import com.web.tests.ifusion.Source;
//import com.web.tests.ifusion.SourceDP;
//
//public class HealthCheckTracert {
//	
//	
//
//	Logger logger = LogManager.getLogger(HealthCheckTracert.class.getName());
//	String scriptfileloc;
//	String configfileloc;
//
//	/**
//	 * Inits the
//	 *
//	 * @throws Exception
//	 * @throws FileNotFoundException
//	 */
//	@Parameters({ "scriptfile", "configfile" })
//	@BeforeClass(alwaysRun = true, groups = { "Smoke", "Sanity" })
//	public void init(String scriptfile, String configfile) throws Exception {		
//		scriptfileloc = scriptfile;
//		configfileloc = configfile;		
//		
//	}
//
//	/*************************************************************************
//	 *
//	 * TEST SUITE TESTS
//	 *
//	 *************************************************************************/
//
//	/*
//	 * * Data Providers list for Modules
//	 * ****************************************
//	 */
//
////	@DataProvider(name = "LoginDP")
////	public Object[][] LoginDP() {
////		if ("firefox".equalsIgnoreCase(browserName)) {
////			return LoginDP.createDP("DR1");
////		} else if ("chrome".equalsIgnoreCase(browserName)) {
////			return LoginDP.createDP("DR1");
////		} else if ("ie".equalsIgnoreCase(browserName)) {
////			return LoginDP.createDP("DR1");
////		} else if ("phanomjs".equalsIgnoreCase(browserName)) {
////			return LoginDP.createDP("DR1");
////		}
////
////		return null;
////	}
//	@Test(groups = "Smoke", priority = 1)
//	public void IPTraceAndValiadte(ITestContext context) {
//		Properties props = new Properties();
//		props.put("python.path","D:/streamlined/HarmonyCoreiFusion/target/test-classes/");
//		props.put("python.home","D:/poc/jython/jython2.7.0");
//		props.put("python.console.encoding", "UTF-8"); // Used to prevent: console: Failed to install '': java.nio.charset.UnsupportedCharsetException: cp0.
//		props.put("python.security.respectJavaAccessibility", "false"); //don't respect java accessibility, so that we can access protected members on subclasses
//		props.put("python.import.site","false");
//
//		//Properties preprops = System.getProperties();
//		String args1[] = {"--input_file",configfileloc}; 
//		PythonInterpreter.initialize(System.getProperties(), props, args1);
//		PythonInterpreter interpreter = new PythonInterpreter();
//		//String script_dir = System.getProperty("user.dir");
//		
//		interpreter.execfile(scriptfileloc);
//		ArrayList<String> r1 = ResultsHolder.getResults();
//		for (int i=0; i<r1.size(); i++) 
//			System.out.println("Line# "+i+" values: "+r1.get(i));
//		//interpreter.execfile(script_dir+"/src/test/resources/pyscripts/tracert.py");
//		
//	}
//
//
//
//	@AfterClass(alwaysRun = true)
//	public void tearDown() {
//
//		System.out.println("***Python script execution Completed***");
//
//		/*try {
//
//			if (driver != null) {
//				driver.quit();
//
//			}
//		} catch (Exception e) {
//			//throw new RuntimeException("teardown() method failed to execute " + e);
//		}*/
//	}	
//
//}