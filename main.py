import pandas as pd
from src.ranker import rank_candidates

def main():
    dataset_file = 'data/monster_com-job_sample.csv'
    
    # Load sample job description from dataset
    try:
        df_dataset = pd.read_csv(dataset_file)
        sample_jd = df_dataset['job_description'].iloc[0]
        sample_title = df_dataset['job_title'].iloc[0]
        print(f"✓ Successfully loaded dataset from '{dataset_file}'")
    except Exception as e:
        print(f"⚠ Could not load dataset file ({e}). Using sample fallback job description.")
        sample_title = "IT Support Technician"
        sample_jd = "Seeking an IT Support Specialist with experience in technical support, LANDesk, Microsoft Office, and Remote Desktop Management Tools."

    # Sample candidate resumes
    candidates = [
        {
            "candidate_id": "Candidate_1 (High Fit - IT Specialist)",
            "resume_text": "Experienced IT Support Technician with 6 years experience in technical support, call tracking software, LANDesk, Microsoft Office, and Remote Desktop Management Tools."
        },
        {
            "candidate_id": "Candidate_2 (Medium Fit - Data Scientist)",
            "resume_text": "Data Scientist proficient in Python, SQL, Machine Learning, Scikit-learn, Pandas, NLP, TF-IDF, and Data Analysis. Experienced with Git and Flask."
        },
        {
            "candidate_id": "Candidate_3 (Low Fit - General Tech)",
            "resume_text": "Junior entry-level assistant with basic knowledge of Excel, Microsoft Office, communication skills, and general office support."
        }
    ]

    print(f"\n==========================================")
    print(f" JOB ROLE: {sample_title}")
    print(f"==========================================\n")
    
    df_ranked, extracted_jd_skills = rank_candidates(candidates, sample_jd)
    
    print("Detected Job Skills:", list(extracted_jd_skills))
    print("\n--- CANDIDATE RANKING TABLE ---")
    print(df_ranked[['Candidate ID', 'Match Score (%)', 'Skill Coverage', 'Missing Skills']].to_string(index=True))

if __name__ == "__main__":
    main()