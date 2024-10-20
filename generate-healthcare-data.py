import pandas as pd
import random
import uuid


# Function to generate random genomic data
def generate_genomic_data(num_samples):
    platforms = ['Illumina', 'PacBio', 'Oxford Nanopore']
    genomic_data = []
    for i in range(num_samples):
        sample_id = random.randint(10000, 99999)
        bam_filename = f'sample{sample_id}.bam'
        md5 = uuid.uuid4().hex
        study = random.choice(['Study_A', 'Study_B', 'Study_C'])
        platform = random.choice(platforms)
        total_bases = random.randint(4000000, 10000000)
        mapped_bases = int(total_bases * random.uniform(0.8, 0.99))
        total_reads = random.randint(800000, 2000000)
        mapped_reads = int(total_reads * random.uniform(0.75, 0.98))
        properly_paired_reads = int(mapped_reads * random.uniform(0.9, 0.99))
        mismatched_bases = round(random.uniform(1.5, 3.5), 2)
        avg_quality = random.randint(25, 35)
        insert_size_mean = random.randint(400, 600)
        insert_size_sd = random.randint(15, 30)
        duplicate_reads = int(mapped_reads * random.uniform(0.04, 0.08))
        duplicate_bases = int(duplicate_reads * random.uniform(0.85, 0.95))

        genomic_data.append([
            bam_filename, md5, study, sample_id, platform, total_bases, mapped_bases,
            total_reads, mapped_reads, properly_paired_reads, mismatched_bases,
            avg_quality, insert_size_mean, insert_size_sd, duplicate_reads, duplicate_bases
        ])
    columns = [
        'bam_filename', 'md5', 'study', 'sample_id', 'platform', 'total_bases', 'mapped_bases',
        'total_reads', 'mapped_reads', 'properly_paired_reads', 'mismatched_bases (%)',
        'avg_quality', 'insert_size_mean', 'insert_size_sd', 'duplicate_reads', 'duplicate_bases'
    ]
    return pd.DataFrame(genomic_data, columns=columns)


# Function to generate random healthcare transactional data
def generate_healthcare_data(num_records):
    diagnoses = [('I10', 'Hypertension'), ('E11.9', 'Type 2 Diabetes'), ('J45', 'Asthma')]
    procedures = [('99213', 'Office visit'), ('99354', 'Prolonged E&M visit'), ('99214', 'Outpatient consultation')]
    medications = [('Lisinopril', '10 mg'), ('Metformin', '500 mg'), ('Albuterol', '100 mcg')]
    doctors = [('Dr. Smith', 'Cardiology'), ('Dr. Lee', 'Endocrinology'), ('Dr. Brown', 'Pulmonology')]
    hospitals = ['City Hospital', 'General Hospital', 'Specialty Clinic']

    healthcare_data = []
    for i in range(num_records):
        patient_id = random.randint(10000, 99999)
        visit_id = f'V{random.randint(100000, 999999)}'
        visit_date = pd.to_datetime(f'2024-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}')
        diagnosis_code, diagnosis_desc = random.choice(diagnoses)
        procedure_code, procedure_desc = random.choice(procedures)
        insurance_claim = f'CLM{random.randint(100000, 999999)}'
        claim_amount = round(random.uniform(200, 1000), 2)
        medication, dosage = random.choice(medications)
        prescribing_doctor, doctor_specialty = random.choice(doctors)
        hospital_name = random.choice(hospitals)

        healthcare_data.append([
            patient_id, visit_id, visit_date, diagnosis_code, diagnosis_desc,
            procedure_code, procedure_desc, insurance_claim, claim_amount,
            medication, dosage, prescribing_doctor, doctor_specialty, hospital_name
        ])

    columns = [
        'patient_id', 'visit_id', 'visit_date', 'diagnosis_code', 'diagnosis_desc',
        'procedure_code', 'procedure_desc', 'insurance_claim', 'claim_amount',
        'medication', 'dosage', 'prescribing_doctor', 'doctor_specialty', 'hospital_name'
    ]
    return pd.DataFrame(healthcare_data, columns=columns)


# Generate larger datasets
genomic_data = generate_genomic_data(1000)
healthcare_data = generate_healthcare_data(1000)

# Display the first few rows of each dataset
genomic_data.head(), healthcare_data.head()
