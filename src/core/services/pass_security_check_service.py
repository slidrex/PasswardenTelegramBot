import math
import pwnedpasswords

class SecurityStatus:
    EXCELLENT = "EXCELLENT"
    OK = "OK"
    WEAK = "WEAK"

class SecurityReport:
    leaked_count:int
    status:SecurityStatus
    entropy: int



def get_entropy(password):
    char_set = set(password)
    char_set_size = len(char_set)
    password_size = len(password)
    entropy = math.log2(char_set_size ** password_size)
    return entropy

def get_security_report(password: str) -> SecurityReport:
    entropy = get_entropy(password)
    
    report = SecurityReport()

    report.leaked_count = pwnedpasswords.check(password)

    if report.leaked_count == 0 and entropy >= 100:
        report.status = SecurityStatus.EXCELLENT
    
    elif report.leaked_count == 0 and 40 < entropy < 100:
        report.status = SecurityStatus.OK
    
    elif report.leaked_count > 0 or entropy < 40:
        report.status = SecurityStatus.WEAK
    
    report.entropy = entropy

    return report
