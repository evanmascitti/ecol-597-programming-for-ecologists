- An extremely frustrating afternoon

- Windows cmd sucks the donkey dick

- Running terminal code in R Studio is also not that great 

- mind your workign directory at all times 

**IMPORTANT**: do NOT use the `.open` command when you are about to call a csv file. This command is only for 'opening' existing databases. To create your own, you need to first build the schema before doing anything else, then check that it is there with `.tables` and _then_ you can use `.import` to pass the file to the empty shema. **FINALLY** call `.save [filepath]` to save as a database. 
