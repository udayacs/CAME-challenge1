public class Sort{
    public static void main(String[] args){

        int[] intArray = new int[args.length];
        System.out.print("Input: [ ");
        int a = 0;
        for (String i : args) {
            System.out.print(i + " ");
            try {
                intArray[a++] = Integer.parseInt(i);
            }
            catch(Exception ex) {
                continue;
            }
        }
        System.out.print("]\n");

        int[] sorted = sortInt(intArray); 
        System.out.print("Output: [ ");
        for (int i : sorted) {
            System.out.print(i + " ");
        }
        System.out.print("]\n");
    }

    private static int[] sortInt(int[] num) {
        if(num.length == 1) {
            return num;
        }

        int devider = 0;
        if((num.length % 2) == 0) {
            devider = num.length/2;
        }
        else {
            devider = (num.length + 1)/2;
        }

        int[] h1Arr = new int[devider];
        int[] h2Arr = new int[num.length - devider];

        for(int a = 0; a < devider; a++){
            h1Arr[a] = num[a];
            if((num.length - devider) > a){
                h2Arr[a] = num[a+devider];
            }
        }

        return merge(sortInt(h1Arr), sortInt(h2Arr) , devider);
    }

    private static int[] merge(int[] a1, int[] a2 , int d) {
        int[] fullarr = new int[a1.length + a2.length];
        int a1Ind = 0, a2Ind = 0, fullarrInd = 0;

        //System.out.print("Intermediate:" + d + "  [ ");
        while (fullarrInd < fullarr.length) {
            if(a1[a1Ind] < a2[a2Ind]) {
                fullarr[fullarrInd] = a1[a1Ind];
                //System.out.print(fullarr[fullarrInd] + " ");
                if(a1Ind < (a1.length - 1)){
                    a1Ind++;
                }
                else {
                    for (int x = a2Ind; x < a2.length; x++) {
                        fullarr[++fullarrInd] = a2[x];
                        //System.out.print(fullarr[fullarrInd] + " ");
                    }
                    break;
                }
            }
            else {
                fullarr[fullarrInd] = a2[a2Ind];
                //System.out.print(fullarr[fullarrInd] + " ");
                if(a2Ind < (a2.length - 1)){
                    a2Ind++;
                }
                else {
                    for (int x = a1Ind; x < a1.length; x++) {
                        fullarr[++fullarrInd] = a1[x];
                        //System.out.print(fullarr[fullarrInd] + " ");
                    }
                    break;
                }
            }
            fullarrInd++;
        }
        //System.out.print("]\n");

        return fullarr;
    }
}