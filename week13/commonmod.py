#!/usr/bin/python3.4
   # Written by Anirudh Anand (lucif3r) : email - anirudh@anirudhanand.com
   # This program will help to decrypt cipher text to plain text if you have
   # more than 1 cipher text encrypted with same Modulus (N) but different
   # exponents. We use extended Euclideangm Algorithm to achieve this.

import gmpy2
import codecs

class RSAModuli:
       def __init__(self):
           self.a = 0
           self.b = 0
           self.m = 0
           self.i = 0
       def gcd(self, num1, num2):
           """
           This function os used to find the GCD of 2 numbers.
           :param num1:
           :param num2:
           :return:
           """
           if num1 < num2:
               num1, num2 = num2, num1
           while num2 != 0:
               num1, num2 = num2, num1 % num2
           return num1
       def extended_euclidean(self, e1, e2):
           """
           The value a is the modular multiplicative inverse of e1 and e2.
           b is calculated from the eqn: (e1*a) + (e2*b) = gcd(e1, e2)
           :param e1: exponent 1
           :param e2: exponent 2
           """
           self.a = gmpy2.invert(e1, e2)
           self.b = (float(self.gcd(e1, e2)-(self.a*e1)))/float(e2)
       def modular_inverse(self, c1, c2, N):
           """
           i is the modular multiplicative inverse of c2 and N.
           i^-b is equal to c2^b. So if the value of b is -ve, we
           have to find out i and then do i^-b.
           Final plain text is given by m = (c1^a) * (i^-b) %N
           :param c1: cipher text 1
           :param c2: cipher text 2
           :param N: Modulus
           """
           i = gmpy2.invert(c2, N)
           mx = pow(c1, self.a, N)
           my = pow(i, int(-self.b), N)
           self.m= mx * my % N
       def print_value(self):
           print("Plain Text: ", codecs.decode(str(hex(self.m)[2:]), "hex"))


def main():
       c = RSAModuli()
       N=189218773141291149531902532213881238723097668486230711045519126662410967963383577654968353248781251634675548209202395462286307056655926283245604600684821710441690531490085204088794241110076717281163750375882083021280346058586455346134359956343167642601364017775778913264957908461925167348987132834110343364485840578364240204481764957299001971535831022203598394476267134507445584729003483674477548966769176435655751139855669196947135054356409591553191400253693397916103452200101794777078113785008653214444899908496569022151673365216008172574687431999622353734350680380954829509387655800799689002928538485899891536328923824833871938226569028688477965963282017397220327492089038492673715752536586499698264109315032613616383651266666427541431357702303363270152591129712292065852336346541914319498540755070157218851050204219233600521769362046214401796834116368827716127188459638431848828777595174590591652747026875740701820000529947909734457613094546613866231519351419987483253867686577260299602041122487972669755787408310317693620777147269079375954836101559764020145652883306546284892204357771270752363408156408859578839123922348880722303244170024935584178231824075468868609932179302726820452342110870684579043564597641407321212053174673
       c1=121529731457722588254451348470154689202431411724113335406912796422671598704822304779718859605534295720813505019562895362393508012341702947874429528373506302075958336702716139114653442999257870876114671352564845723456700541479663793591020246457763022776169671892215035608486946486352167572150487511875514259031434691224542816657640393068965254373385648061953728810036999251746504040300373668371175672563760233715187929729879587056420285881382366083743384905548153364804704275060209282738818364696980867445839669910461623756537990697937550127760004035024875564961452060740203402961968510814521579346707752623168247417104236401853714897092572346644777337160719123696426937080015449916298747458728517993969032186195764852407297159960253534872990619687962449942418037644244941345827809671478128332188414100129440068026503976480699915229217346860738616892354461876301014310029871783031732375804922633033410382491107085083644957149586307998536397527201057780925615067823631144589916844485543826817545974482763036378802590044183989961391431102520804151948126187994255875172050214692146855531141077250887824574650917978891407021979031672496225644462567145296570033919732360781287276868243639900632803983479543238587442343376343966680443889465
       c2=129067612681173668176406342282948818177022271158629153115383646448683823157632838480862224701398533180072049616970386563426405435157608501054357839943711162754225492621251763596363779750273918160085538888877158303907079960353250952018712553432142562346365892304583668342422195481960448035653781786368503726683290582317513548716808429167815303792429608516079977552864337971436677491988480214260794154222405712881991161684666813243313506806815077118892562284376124534552103184277377036356388529150999260710681330179536684957113768061427711656639389461308926989685809105932102616668916120552637165927013016742052250438403345080098559842260141469593778751303203011444697743548160068812615920919192068812835781543551427503210980551231067994578070759473705589971737883178278280371135398704082833651346534177183172841466835574388510126015572080910400721322472865670289736696387045207275361342201523374562366570097825437393739999494653060965243765408720064973487078941853504887197045675692438716484086011754378224244839723088164080160218303176175257596995633109370568611033217652241577966712062759296655988457652926393446569065742761743484363792544799196604738179359674438442522538071307787109934522969823959605432067447484786682216492436446
       e1=257
       e2=65537
       c.extended_euclidean(e1, e2)
       c.modular_inverse(c1, c2, N)
       c.print_value()

if __name__ == '__main__':
       main()