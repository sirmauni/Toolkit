# toolkit configuration class

import yaml
import os

class TLKConfig:

    tConfig = None

    def __init__(self):
        with open("./toolkit_config.yaml") as config_yaml:
            self.tConfig = yaml.safe_load(config_yaml)

        # check if any tools were passed
        if self.tConfig["tools"] == None or len(self.tConfig["tools"]) <= 0:
            raise Exception("No tools found")

        # for each tool,
        RecordedToolNames = []
        for tool in self.tConfig["tools"]:
            # check if tool has already been recorded
            for toolName in RecordedToolNames:
                if toolName == tool:
                    raise Exception("Duplicate configuration for tool '" + toolName + "'")

            # check if tool conflicts with reserved name
            for reservedWord in ["help", "list", "info"]:
                if tool.lower() == reservedWord:
                    raise Exception("Tool '" + tool + "' conflicts with reserved terms")
                
            # check if tool executable file exists
            if self.tConfig["tools"][tool]["exec"] == None:
                raise Exception("No executable described for tool (" + tool + ")")
            
            if len(self.tConfig["tools"][tool]["exec"]) <= 0:
                raise Exception("No executable described for tool (" + tool + ")")
            
            # check if executable file exists
            if os.path.exists(self.tConfig["tools"][tool]["exec"]) != True:
                raise Exception("Executable '" + tool + "' not found")
            
            # check if tool minimum number of arguments is valid
            if type(self.tConfig["tools"][tool]["minArgs"]) != int:
                raise Exception("Expected value type 'int', Found '" + type(self.tConfig["tools"][tool]["minArgs"]) + "'")
            
            # record tool name 
            RecordedToolNames.append(tool)
            
    def getSupportedToolCount(self):
        if self.tConfig != None:
            return len(self.tConfig["tools"])
        else:
            return "Unable to locate toolkit configuration"
        
    def toolExists(self, toolName):
        for tool in self.tConfig["tools"]:
            if tool == toolName:
                return True
        
        return False
        
    def getToolInfo(self, toolName):
        # check if tool exist
        if self.toolExists(toolName) != True:
            raise Exception("Tool '" + toolName + "' Does Not Exists")
        
        # print data for tool
        ToolInfo = "Tool '" + toolName + "' Info:\n"
        for toolAttr in self.tConfig["tools"][toolName]:
            ToolInfo = ToolInfo + "\t" + toolAttr + ": " + str(self.tConfig["tools"][toolName][toolAttr]) + "\n"

        return ToolInfo

    def getToolExecutable(self, toolName):
        # check if tool exist
        if self.toolExists(toolName) != True:
            raise Exception("Tool '" + toolName + "' Does Not Exists")
        
        # fetch executable dir
        return self.tConfig["tools"][toolName]["exec"]

    def getToolMinArguments(self, toolName):
        # check if tool exist
        if self.toolExists(toolName) != True:
            raise Exception("Tool '" + toolName + "' Does Not Exists")
        
        # check if min number of arguments present
        if self.tConfig["tools"][toolName]["minArgs"] == None or type(self.tConfig["tools"][toolName]["minArgs"]) != int:
            return 0
        else:
            return self.tConfig["tools"][toolName]["minArgs"]