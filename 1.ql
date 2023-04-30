{
    "extractor_root" : "/home/user/codeql/java",
    "extractor_options" : {
        "option1" : {
            "title" : "Java extractor option 1",
            "description" : "An example string option for the Java extractor.",
            "type" : "string",
            "pattern" : "[a-z]+"
        },
        "group1" : {
            "title" : "Java extractor group 1",
            "description" : "An example option group for the Java extractor.",
            "type" : "object",
            "properties" : {
                "option2" : {
                    "title" : "Java extractor option 2",
                    "description" : "An example array option for the Java extractor",
                    "type" : "array",
                    "pattern" : "[1-9][0-9]*"
                }
            }
        }
    }
}