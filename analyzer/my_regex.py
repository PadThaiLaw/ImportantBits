#!/usr/bin/env python

import re

str = """[39]                          To achieve this purpose, Board hearings tend to be less formal than criminal trials.  The Board is not bound by traditional rules of evidence:  IRPA, at s. 170(g) and (h); Thamotharem v. Canada (Minister of Citizenship and Immigration), 2007 FCA 198 (CanLII), [2008] 1 F.C.R. 385, at para. 41; Kumar v. Canada (Citizenship and Immigration), 2009 FC 643 (CanLII), at paras. 28-29.  Section 162(2) of the IRPA instructs each division of the Board to “deal with all proceedings before it as informally and quickly as the circumstances and the considerations of fairness and natural justice permit”.

[73]           For the purposes of the above taxonomy, these two types of abuse of discretion are best regarded as matters of substantive unacceptability. Some analyze these as independent nominate grounds of automatic review – if decision-makers do these things, their decisions are automatically invalid: see Thamotharem v. Canada (Minister of Citizenship and Immigration), 2007 FCA 198 (CanLII), [2008] 1 F.C.R. 385. Others view these as examples of decisions that are outside the Dunsmuir range of acceptability or defensibility: Stemijon Investments Ltd., supra at paragraphs 20-24. Regardless of how these are analyzed, they are claims that sound in administrative law.

[59]           Policy statements play a useful and important role in administration: Thamotharem v. Canada (Minister of Citizenship and Immigration), 2007 FCA 198 (CanLII), [2008] 1 F.C.R. 385. For example, by encouraging the application of consistent principle in decisions, policy statements allow those subject to administrative decision-making to understand how discretions are likely to be exercised. With that understanding, they can better plan their affairs.

[60]           However, as explained in paragraphs 20-25 above, decision-makers who have a broad discretion under a law cannot fetter the exercise of their discretion by relying exclusively on an administrative policy: Thamotharem, supra at paragraph 59; Maple Lodge Farms, supra at page 6; Dunsmuir, supra (as explained in paragraph 24 above). An administrative policy is not law. It cannot cut down the discretion that the law gives to a decision-maker. It cannot amend the legislator’s law. A policy can aid or guide the exercise of discretion under a law, but it cannot dictate in a binding way how that discretion is to be exercised.

[48]           The Federal Court of Appeal adopted this principle in Thamotharem v. Canada (Minister of Citizenship and Immigration), 2007 FCA 198 (CanLII), [2008] 1 F.C.J. 385, at paragraph 61:

It is fundamental to the idea of justice that adjudicators, whether in administrative tribunals or courts, strive to ensure that similar cases receive the same treatment. This point was made eloquently by Gonthier J. when writing for the majority in IWA v. Consolidated‑Bathurst Packaging Ltd., 1990 CanLII 132 (SCC), 1990] 1 S.C.R. 282, at page 327 (Consolidated‑Bathurst) . . . " """


def find_paragraphs(casename, text):
  re_to_try = []
  # re_to_try.append(re.compile("Thamotharem.*para[s|.| ]*([0-9]+)-([0-9]+)")) # group(1) && group(2)
  re_to_try.append(re.compile(casename+".*para[s|.| ]*([0-9]+)"))
  re_to_try.append(re.compile(casename+".*paragraphs* +([0-9]+)"))

  for attempt in re_to_try:
    result = attempt.search(text)
    if (result != None) and result.group(1):
      return result.group(1)

    return None

print(find_paragraphs("Thamotharem", str))
