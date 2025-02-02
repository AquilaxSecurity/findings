public function verifyResetToken(Request $request) {
   $request->validate([
      'email' => 'required|email',
      'token' => 'required'
   ]);

   $email = $request->input('email');
   $token = $request->input('token');

   $resetRecord = DB::table('password_resets')->where('email', $email)->first();

   if (!$resetRecord || Carbon::parse($resetRecord->created_at)->isPast()) {
       return response()->json(['message' => 'Invalid or expired token'], 400);
   }
   if (!Hash::check($token, $resetRecord->token)) {
       return response()->json(['message' => 'Invalid token'], 400);
   }

   return response()->json(['message' => 'Token verified. Proceed to reset password.']);
}
