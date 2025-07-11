import boto3
import os
from datetime import datetime

# Set up AWS session and clients
session = boto3.Session()
iam = session.client('iam')
s3 = session.client('s3')

# Create reports folder if missing
if not os.path.exists("reports"):
    os.makedirs("reports")

# Logging function with timestamps
def write_report(message, filename="reports/security_report.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a") as file:
        file.write(f"[{timestamp}] {message}\n")

# Scan IAM users
def list_iam_users():
    print("\n🔐 IAM Users:")
    try:
        response = iam.list_users()
        if not response['Users']:
            msg = "No IAM users found."
            print(msg)
            write_report(msg)
        for user in response['Users']:
            msg = f"User: {user['UserName']}"
            print(msg)
            write_report(msg)
    except Exception as e:
        error = f"Error listing IAM users: {e}"
        print(error)
        write_report(error)

# Scan S3 buckets for public access via ACL
def scan_s3_buckets():
    print("\n🗂️ S3 Bucket Scan:")
    try:
        response = s3.list_buckets()
        if not response['Buckets']:
            msg = "No S3 buckets found."
            print(msg)
            write_report(msg)
        for bucket in response['Buckets']:
            name = bucket['Name']
            try:
                acl = s3.get_bucket_acl(Bucket=name)
                for grant in acl['Grants']:
                    grantee = grant.get('Grantee', {})
                    if grantee.get('URI') == 'http://acs.amazonaws.com/groups/global/AllUsers':
                        alert = f"[!] Public bucket: {name}"
                        print(alert)
                        write_report(alert)
            except Exception as e:
                error = f"Error checking {name}: {e}"
                print(error)
                write_report(error)
    except Exception as e:
        error = f"Error listing buckets: {e}"
        print(error)
        write_report(error)

# Entry point
if __name__ == "__main__":
    print("🛡️ Starting AWS Security Scan...\n")
    list_iam_users()
    scan_s3_buckets()
    print("\n✅ Scan Complete! Results saved in 'reports/security_report.txt'")