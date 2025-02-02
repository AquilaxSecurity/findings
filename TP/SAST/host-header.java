public function resetPassword(Request $request) {

   $request->validate([
     'email' => 'required|email',
]);

   $host = $request->header ('host');
   $email = $request->input('email');

   $token = Str:: random (60);
   $resetLink = "https://{$host}/reset-password?token={$token}";

   PasswordReset:: create([
   'email' => $email,
   'token' => $token,
   'created_at' = now(),
]);

Mail:: to($email)->send(new ResetPasswordMail($resetLink));

return response()->json([
    'message' => 'A password reset link has been sent to your email.'
]);
}
