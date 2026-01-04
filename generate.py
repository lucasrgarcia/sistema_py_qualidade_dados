import pandas as pd
import random
import logging
from pathlib import Path
from datetime import datetime, timedelta
from dataclasses import dataclass

# LOGS

logging.basicConfig(
    filename="data_quality.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


# 1 - GERADOR DE DADOS


def random_date(start, end):
    delta = end - start
    return start + timedelta(days=random.randint(0, delta.days))

def generate_customer_data(n_rows=300):
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)

    records = []

    for i in range(1, n_rows + 1):
        age = random.choice([random.randint(18, 90), -5, 150])
        income = random.choice([random.randint(2000, 15000), None, -1000])
        country = random.choice(["BR", "US", "DE", None])

        signup_date = random.choice([
            random_date(datetime(2022, 1, 1), datetime(2024, 1, 1)).strftime("%Y-%m-%d"),
            "2023-02-30",
            "invalid_date"
        ])

        email = random.choice([
            f"user{i}@mail.com",
            "duplicado@mail.com"
        ])

        records.append({
            "customer_id": i if random.random() > 0.05 else 10,
            "age": age,
            "income": income,
            "country": country,
            "signup_date": signup_date,
            "email": email
        })

    pd.DataFrame(records).to_csv(data_dir / "input.csv", index=False)

# 2 - VALIDAÇÃO

@dataclass
class ValidationResult:
    rule_name: str
    passed: bool
    error_count: int
    description: str
    severity: str  # ERROR / WARNING


# 3 - VALIDAÇÕES


def validate_nulls(df, columns):
    errors = df[columns].isnull().sum().sum()
    return ValidationResult(
        "Null Values Check",
        errors == 0,
        int(errors),
        f"{errors} valores nulos encontrados",
        "WARNING"
    )

def validate_age_range(df, min_age=18, max_age=90):
    invalid = df[(df["age"] < min_age) | (df["age"] > max_age)]
    return ValidationResult(
        "Age Range Check",
        invalid.empty,
        len(invalid),
        f"{len(invalid)} idades fora do intervalo permitido",
        "ERROR"
    )

def validate_customer_id_duplicates(df):
    duplicates = df.duplicated(subset=["customer_id"]).sum()
    return ValidationResult(
        "Customer ID Duplicates",
        duplicates == 0,
        int(duplicates),
        f"{duplicates} customer_id duplicados",
        "ERROR"
    )

def validate_email_duplicates(df):
    duplicates = df.duplicated(subset=["email"]).sum()
    return ValidationResult(
        "Email Duplicates",
        duplicates == 0,
        int(duplicates),
        f"{duplicates} emails duplicados",
        "ERROR"
    )

def validate_signup_date(df):
    invalid_dates = pd.to_datetime(
        df["signup_date"],
        format="%Y-%m-%d",
        errors="coerce"
    ).isna().sum()
    return ValidationResult(
        "Signup Date Validity",
        invalid_dates == 0,
        int(invalid_dates),
        f"{invalid_dates} datas inválidas encontradas",
        "WARNING"
    )

# 3.5 -  MELHORIA DE QUALIDADE

def improve_data_quality(df):
    df = df.copy()

    df = df.drop_duplicates(subset=["customer_id"])
    df = df.drop_duplicates(subset=["email"])

    df.loc[(df["age"] < 18) | (df["age"] > 90), "age"] = None
    df.loc[df["income"] < 0, "income"] = None
    df["country"] = df["country"].fillna("UNKNOWN")

    df["signup_date"] = pd.to_datetime(
        df["signup_date"],
        format="%Y-%m-%d",
        errors="coerce"
    )

    return df


# 4 - PIPELINE


class DataValidationPipeline:
    def __init__(self, df):
        self.df = df
        self.results = []

    def add_rule(self, rule):
        self.results.append(rule(self.df))

    def run(self):
        return self.results


# 5 - RELATÓRIO E LOG

def generate_report(results):
    return pd.DataFrame([{
        "Rule": r.rule_name,
        "Severity": r.severity,
        "Status": "PASS" if r.passed else "FAIL",
        "Errors": r.error_count,
        "Description": r.description
    } for r in results])

def log_results(results, stage):
    for r in results:
        msg = f"{stage} | {r.rule_name} | {r.severity} | {r.description}"
        if r.passed:
            logging.info(msg)
        else:
            logging.error(msg)


# 6 - EXECUÇÃO


def main():
    generate_customer_data()
    df_raw = pd.read_csv("data/input.csv")

    # BEFORE
    pipeline_before = DataValidationPipeline(df_raw)
    pipeline_before.add_rule(lambda df: validate_nulls(df, ["income", "country"]))
    pipeline_before.add_rule(validate_age_range)
    pipeline_before.add_rule(validate_customer_id_duplicates)
    pipeline_before.add_rule(validate_email_duplicates)
    pipeline_before.add_rule(validate_signup_date)

    results_before = pipeline_before.run()
    report_before = generate_report(results_before)
    report_before.to_csv("data/report_before.csv", index=False)
    log_results(results_before, "BEFORE")

    print("\nRELATÓRIO - ANTES\n")
    print(report_before)

    # AFTER
    df_improved = improve_data_quality(df_raw)

    pipeline_after = DataValidationPipeline(df_improved)
    pipeline_after.add_rule(lambda df: validate_nulls(df, ["income", "country"]))
    pipeline_after.add_rule(validate_age_range)
    pipeline_after.add_rule(validate_customer_id_duplicates)
    pipeline_after.add_rule(validate_email_duplicates)
    pipeline_after.add_rule(validate_signup_date)

    results_after = pipeline_after.run()
    report_after = generate_report(results_after)
    report_after.to_csv("data/report_after.csv", index=False)
    log_results(results_after, "AFTER")

    print("\nRELATÓRIO - DEPOIS\n")
    print(report_after)

if __name__ == "__main__":
    main()
