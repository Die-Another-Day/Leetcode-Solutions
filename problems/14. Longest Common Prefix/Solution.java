class Solution {
    public String longestCommonPrefix(String[] strs) {
        if(strs == null || strs.length==0){
            System.out.println("String is mpt");
            return "";
        }
        String str = strs[0];
        for(int i = 1; i<strs.length;i++){
            while(strs[i].indexOf(str)!=0){
                str = str.substring(0,str.length()-1);
                if(str.isEmpty()){
                    return "";
                }
            }
        }
        //System.out.println(str);
        return str;

    }
        
}

